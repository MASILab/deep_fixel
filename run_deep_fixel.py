import fissile
from datetime import datetime

lr = 1e-3
batch_size = 512
n_steps = 10000
validation_patience = 5
loss = "MSE"
model = "mesh_mlp"
gpu_id = 1
seed = 42
mesh_subdivide = 3
kappa = 100
n_fibers = 'both'
save_dir = "./models"
test_dir = "./test_data"

datetime_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
name = f"deepfixel_{model}_{datetime_str}"

fissile.train_mesh_model(
    run_name=name,
    lr=lr,
    batch_size=batch_size,
    n_steps=n_steps,
    validation_patience=validation_patience,
    loss_name=loss,
    model=model,
    gpu_id=gpu_id,
    seed=seed,
    mesh_subdivide=mesh_subdivide,
    kappa=kappa,
    n_fibers=n_fibers,
    save_dir=save_dir,
)

output_dir = f'./outputs/{name}'
amp_threshold = 0.1
model_path = f"./models/{name}/best_model.pth"

fissile.test_mesh_model(
    model_path=model_path,
    batch_size=batch_size,
    n_fibers=n_fibers,
    subdivide_mesh=mesh_subdivide,
    amp_threshold=amp_threshold,
    output_dir=output_dir,
    kappa=kappa,
    test_dir=test_dir,
    gpu_id=gpu_id,
)