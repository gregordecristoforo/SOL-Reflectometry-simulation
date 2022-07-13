import matplotlib.pyplot as plt
from cut_off_layer import calculate_cut_off_layer
from define_model import define_model

bm = define_model(2)

ds = bm.make_realization(file_name="time_series.nc", speed_up=True, error=1e-2)
ds.n.isel(x=3).plot()
plt.show()


cut_off_layer_positions = calculate_cut_off_layer(ds, 2)
plt.plot(cut_off_layer_positions)
plt.show()
