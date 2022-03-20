# Import libraries
from flask import Flask
from flask_restful import Api, Resource, reqparse, fields, marshal_with, abort
from dataframe_handler import DfHandler

# Initialization for FLASK server
app = Flask(__name__)
api = Api(app)

# Define arguments needed
iso_countries_post_args = reqparse.RequestParser()
iso_countries_post_args.add_argument("iso",
                                     type=str,
                                     help="Country ISO code required",
                                     required=True)
iso_countries_post_args.add_argument("countries",
                                     type=str,
                                     action='append',
                                     help="Countries to compare with are required",
                                     required=True)

# Format for response return
response_fields = {
    'iso' : fields.String,
    'match_count': fields.Integer,
    'matches': fields.List(fields.String)
}

class MatchCountry(Resource):
    """Class for Match Country microservice

    The microservice is able to take a country ISO code and a list of country names (in different languages)
    as an input. It will filter out just the countries that correspond to the provided ISO code and return
    them to the output.

    """

    @marshal_with(response_fields)
    def post(self):
        """Define POST request."""
        # Set up variables
        args = iso_countries_post_args.parse_args()
        df_handler = DfHandler()
        country = df_handler.get_country_from_iso(args["iso"])
        # If country exists, try to find the matching names
        if country is not None:
            diff_lang = df_handler.get_country_diff_lang(country.name)
            if diff_lang.empty:
                # Abort if nothing is found
                abort(404, message=f"Could not find specified country name, {country.name}, in different languages")
            countries_match = df_handler.get_matching_names(diff_lang, args["countries"])
        else:
            # Abort if ISO code is not valid
            abort(404, message="Country ISO code is not valid...")

        # Prepare response fields
        iso_code = country.alpha_3
        match_count = len(countries_match)
        result = {"iso": iso_code,
                  "match_count": match_count,
                  "matches": countries_match}
        return result

# Add resource through /match_country URL
api.add_resource(MatchCountry, "/match_country")

if __name__ == "__main__":
    app.run(debug=True)
