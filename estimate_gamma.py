from define_model import define_model
import matplotlib.pyplot as plt
import numpy as np
import closedexpressions as ce
import fppanalysis as fa

bm = define_model(2)

ds = bm.make_realization(file_name="time_series.nc", speed_up=True, error=1e-2)
for i in range(5):
    time_series = np.array(ds.n.isel(x=i).values)[0]
    time_series = (time_series - time_series.mean()) / time_series.std()
    bin_centers, hist = fa.get_hist(time_series, 64)
    plt.semilogy(bin_centers, hist)

plt.semilogy(bin_centers, ce.norm_shot_noise_dist(bin_centers, g=2), label="fit")
plt.legend()
plt.show()
