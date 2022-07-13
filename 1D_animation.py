from blobmodel import Model, show_model, DefaultBlobFactory

bf = DefaultBlobFactory(A_dist="exp", W_dist="deg", vx_dist="deg", vy_dist="zeros")

bm = Model(
    Nx=500,
    Ny=1,
    Lx=10,
    Ly=0,
    dt=0.1,
    T=100,
    periodic_y=False,
    blob_shape="exp",
    num_blobs=300,
    t_drain=10,
    blob_factory=bf,
)

ds = bm.make_realization(speed_up=True, error=1e-2)
show_model(dataset=ds, interval=100, save=True)
