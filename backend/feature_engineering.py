import pandas as pd

def feature_engineering(data):

    data_encoded = data.copy()

    data_encoded["curvature"] = pd.cut(
        data["curvature"],
        bins=3,
        labels=["faible", "moyenne", "forte"]
    )

    data_encoded["speed_limit"] = pd.cut(
        data["speed_limit"],
        bins=2,
        labels=["faible", "elevee"]
    )

    col_categorielle = ['road_type', 'lighting', 'weather', 'time_of_day', 'curvature', 'speed_limit']

    encoded = encoder.transform(data_encoded[col_categorielle])
    data_final = pd.DataFrame(encoded, columns=encoder.get_feature_names_out(col_categorielle))
    data_final = pd.concat([data.drop(columns=col_categorielle).reset_index(drop=True), 
                            data_final.reset_index(drop=True)], axis=1)

    
    colonnes_bool = ['road_signs_present', 'public_road', 'holiday', 'school_season']
    data_final[colonnes_bool] = data_final[colonnes_bool].astype('int')
    
    data_final["curvature_speed_interaction"] = data["curvature"] * data["speed_limit"]
    data_final["accidents_per_lane"] = data["num_reported_accidents"] / (data["num_lanes"] + 1e-3)
    data_final["curvature_per_lane"] = data["curvature"] / (data["num_lanes"] + 1e-3)
    data_final["speed_per_lane"] = data["speed_limit"] / (data["num_lanes"] + 1e-3)

    return data_final
