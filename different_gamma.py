from define_model import define_model
import matplotlib.pyplot as plt
import numpy as np
import fppanalysis as fa

bm = define_model(2)
gamma_values = np.linspace(1, 9, 5)
bms = [define_model(i) for i in range(1, 10, 2)]


for i in gamma_values:
    bm = define_model(gamma=i)
    ds = bm.make_realization(file_name="time_series.nc", speed_up=True, error=1e-2)

    time_series = np.array(ds.n.isel(x=3).values)[0]
    time_series = (time_series - time_series.mean()) / time_series.std()
    bin_centers, hist = fa.get_hist(time_series, 64)
    plt.semilogy(bin_centers, hist)

plt.show()
