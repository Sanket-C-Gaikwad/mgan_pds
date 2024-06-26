import argparse
import os

from torch.backends import cudnn

from solver import Solver


def main(config):

    # for fast training
    cudnn.benchmark = True

    # create directories if not exist
    if not os.path.exists(config.log_dir):
        os.makedirs(config.log_dir)
    if not os.path.exists(config.model_save_dir):
        os.makedirs(config.model_save_dir)
    if not os.path.exists(config.sample_dir):
        os.makedirs(config.sample_dir)
    if not os.path.exists(config.result_dir):
        os.makedirs(config.result_dir)

    from dataloader import get_loader

    data_loader = get_loader(
        config.image_dir,
        config.attr_path,
        config.selected_attrs,
        config.attr_dims,
        config.crop_size,
        config.image_size,
        config.batch_size,
        config.mode,
    )

    # run
    solver = Solver(config, data_loader)
    if config.mode == "train":
        solver.train()
    elif config.mode == "test":
        solver.test()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # model configuration
    parser.add_argument("--crop_size",
                        type=int,
                        default=1024,
                        help="image crop size")
    parser.add_argument("--image_size",
                        type=int,
                        default=128,
                        help="image resolution")
    parser.add_argument(
        "--e_conv_dim",
        type=int,
        default=64,
        help="number of conv filters in the first layer of Encoder",
    )
    parser.add_argument(
        "--d_conv_dim",
        type=int,
        default=64,
        help="number of conv filters in the first layer of Discriminator",
    )
    parser.add_argument(
        "--e_repeat_num",
        type=int,
        default=0,
        help="number of residual blocks in Encoder",
    )
    parser.add_argument(
        "--t_repeat_num",
        type=int,
        default=6,
        help="number of residual blocks in Transformer",
    )
    parser.add_argument(
        "--d_repeat_num",
        type=int,
        default=6,
        help="number of strided conv layers in Discriminator",
    )
    parser.add_argument(
        "--lambda_cls",
        type=float,
        default=1,
        help="weight for domain classification loss",
    )
    parser.add_argument("--lambda_cyc",
                        type=float,
                        default=10,
                        help="weight for reconstruction loss")
    parser.add_argument("--lambda_gp",
                        type=float,
                        default=10,
                        help="weight for gradient penalty")
    parser.add_argument(
        "--attr_dims",
        type=list,
        nargs="+",
        default=[3, 1, 1],
        help="separate attributes into different modules",
    )
    parser.add_argument(
        "--selected_attrs",
        # type=list,
        nargs="+",
        default=["red", "green", "blue", "black", "white", "yellow", "basket", "road", "utility", "cargo", "disk_wheel", "racing_handle", "bottle"],
        help="selected attributes for the CelebA dataset",
    )

    # training configuration
    parser.add_argument("--batch_size",
                        type=int,
                        default=16,
                        help="mini-batch size")
    parser.add_argument(
        "--num_epochs",
        type=int,
        default=20,
        help="number of total iterations for training D",
    )
    parser.add_argument(
        "--num_epochs_decay",
        type=int,
        default=10,
        help="number of iterations for decaying lr",
    )
    parser.add_argument("--g_lr",
                        type=float,
                        default=0.00005,
                        help="learning rate for Generation")
    parser.add_argument("--d_lr",
                        type=float,
                        default=0.00005,
                        help="learning rate for Discrimination")
    parser.add_argument("--n_critic",
                        type=int,
                        default=5,
                        help="number of D updates per each G update")
    parser.add_argument("--beta1",
                        type=float,
                        default=0.5,
                        help="beta1 for Adam optimizer")
    parser.add_argument("--beta2",
                        type=float,
                        default=0.999,
                        help="beta2 for Adam optimizer")
    parser.add_argument("--resume_epoch",
                        type=int,
                        default=None,
                        help="resume training from this step")

    # test configuration
    parser.add_argument("--test_epoch",
                        type=int,
                        default=20,
                        help="test model from this step")

    # miscellaneous.
    parser.add_argument("--mode",
                        type=str,
                        default="train",
                        choices=["train", "test"])
    parser.add_argument("--use_tensorboard", type=bool, default=True)

    # directories
    parser.add_argument("--image_dir",
                        type=str,
                        default="./datasets/biked")
    parser.add_argument("--attr_path",
                        type=str,
                        default="./datasets/attribute.txt")
    parser.add_argument("--log_dir", type=str, default="./logs")
    parser.add_argument("--model_save_dir", type=str, default="./models")
    parser.add_argument("--sample_dir", type=str, default="./samples")
    parser.add_argument("--result_dir", type=str, default="./results")

    # step size
    parser.add_argument("--log_step", type=int, default=10)
    parser.add_argument("--sample_step", type=int, default=1000)
    parser.add_argument("--model_save_step", type=int, default=1)
    parser.add_argument("--lr_update_step", type=int, default=1)

    config = parser.parse_args()
    print(config)
    print("\n")
    main(config)
