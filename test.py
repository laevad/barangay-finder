# Define the 'covert' dictionary with two features
covert = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [120.94625672200004, 18.511575597000046],
                        [120.94704360700007, 18.420625793000056],
                        [120.87035669400007, 18.429886047000025],
                        [120.94625672200004, 18.511575597000046],
                    ]
                ],
            },
            "properties": {
                "ADM1_PCODE": "PH010000000",
                "ADM1_EN": "REGION I (ILOCOS REGION)",
                "ADM2_PCODE": "PH012800000",
                "ADM2_EN": "ILOCOS NORTE",
                "ADM3_PCODE": "PH012801000",
                "ADM3_EN": "ADAMS",
                "ADM4_PCODE": "PH012801001",
                "ADM4_EN": "Adams (Pob.)",
            },
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [124.64686322900002, 8.479235199000072],
                        [124.64643236600011, 8.478523338000059],
                        [124.64453406900009, 8.479079090000027],
                        [124.64485253400005, 8.480034482000065],
                        [124.64686322900002, 8.479235199000072],
                    ]
                ],
            },
            "properties": {
                "ADM1_PCODE": "PH100000000",
                "ADM1_EN": "REGION X (NORTHERN MINDANAO)",
                "ADM2_PCODE": "PH104300000",
                "ADM2_EN": "MISAMIS ORIENTAL",
                "ADM3_PCODE": "PH104305000",
                "ADM3_EN": "CAGAYAN DE ORO CITY (Capital)",
                "ADM4_PCODE": "PH104305008",
                "ADM4_EN": "Barangay 12 (Pob.)",
            },
        },
    ],
}

# Create an empty list to store C#-like code for each feature
cs_like_codes = []

# Loop through each feature in the 'covert' dictionary
for feature in covert["features"]:
    # Extracted data from the feature
    coordinates = feature["geometry"]["coordinates"]
    properties = feature["properties"]

    # Create the C#-like code string for this feature
    cs_like_code = f"""new()
{{
    Type = "Feature",
    Geometry = new Geometry
    {{
        Type = "Polygon",
        Coordinates = new List<List<List<double>>>
        {{
"""

    for coord in coordinates[0]:
        cs_like_code += f"""            new List<double>
            {{
                {coord[0]},
                {coord[1]}
            }},
"""

    cs_like_code += f"""        }}
    }},
    Properties = new Properties
    {{
        Adm1En = "{properties["ADM1_EN"]}",
        Adm1Pcode = "{properties["ADM1_PCODE"]}",
        Adm2En = "{properties["ADM2_EN"]}",
        Adm3En = "{properties["ADM3_EN"]}",
        Adm3Pcode = "{properties["ADM3_PCODE"]}",
        Adm4En = "{properties["ADM4_EN"]}",
        Adm4Pcode = "{properties["ADM4_PCODE"]}",
        Province = "Province 1",
        Region = "Region 1"
    }}
}}"""

    # Append the C#-like code to the list
    cs_like_codes.append(cs_like_code)

# Print the C#-like code for each feature
for i, code in enumerate(cs_like_codes, start=1):
    print(code+",")
