from blobmodel import Model, DefaultBlobFactory


def define_model(gamma):
    bf = DefaultBlobFactory(A_dist="exp", W_dist="deg", vx_dist="deg", vy_dist="zeros")
    num_blobs = 1000
    T = num_blobs / gamma
    return Model(
        Nx=100,
        Ny=1,
        Lx=10,
        Ly=0,
        dt=0.01,
        T=T,
        periodic_y=False,
        blob_shape="exp",
        num_blobs=num_blobs,
        t_drain=10,
        blob_factory=bf,
    )
