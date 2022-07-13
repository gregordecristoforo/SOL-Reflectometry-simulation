import xarray as xr
import numpy as np


def calculate_cut_off_layer(ds: xr.Dataset, threshold: float) -> np.ndarray:
    ds["threshold_exceeded"] = ds["n"] > threshold
    reflection_points = []
    for time in ds.t.values:
        tmp = ds.threshold_exceeded.sel(t=time).values
        try:
            indexes_above_threshold = np.where(tmp == True)[1]
            reflection_point = ds.x.isel(x=indexes_above_threshold[-1]).values
        except IndexError:
            reflection_point = ds.x.isel(x=0).values
        reflection_points.append(reflection_point)
    return np.array(reflection_points)
