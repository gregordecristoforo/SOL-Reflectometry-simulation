from blobmodel import Model, DefaultBlobFactory
import matplotlib.pyplot as plt
from reflection_point import calculate_reflection_point

bf = DefaultBlobFactory(A_dist="exp", W_dist="deg", vx_dist="deg", vy_dist="zeros")

bm = Model(
    Nx=100,
    Ny=1,
    Lx=10,
    Ly=0,
    dt=0.01,
    T=100,
    periodic_y=False,
    blob_shape="exp",
    num_blobs=300,
    t_drain=10,
    blob_factory=bf,
)

ds = bm.make_realization(file_name="time_series.nc", speed_up=True, error=1e-2)
ds.n.isel(x=3).plot()
plt.show()


reflection_points = calculate_reflection_point(ds, 3)
plt.plot(reflection_points)
plt.show()
