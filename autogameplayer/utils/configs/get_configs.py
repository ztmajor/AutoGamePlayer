from configargparse import ArgumentParser
# import torch
import os

# from yaml import parse

from autogameplayer.utils.configs import (
    add_config_opts,
    add_general_opts,
    # add_dataset_preprocess_opts,
    # add_train_opts,
    # add_inference_opts,
    # add_model_opts,
    add_reproducibility_opts,
    # add_log_opts,
)


def get_start_config():
    parser = ArgumentParser(description='for start playing game')

    add_config_opts(parser)
    add_general_opts(parser)
    add_reproducibility_opts(parser)
    opts, unknown_opts = parser.parse_known_args()
    if unknown_opts:
        print("unknown_opts:", unknown_opts)

    return opts


# def get_train_config():
#     parser = ArgumentParser(description='train')
#     add_config_opts(parser)
#     add_general_opts(parser)
#     add_train_opts(parser)
#     add_model_opts(parser)
#     add_log_opts(parser, is_train=True)
#     add_reproducibility_opts(parser)
#     opts, unknown_opts = parser.parse_known_args()
#     if unknown_opts:
#         print("unknown_opts:", unknown_opts)

#     opts.device = torch.device(f'cuda:{opts.gpu_id}' if torch.cuda.is_available() else 'cpu')

#     # check
#     opts.save_model = True if opts.save_model_path != "" else False
    
#     if opts.save_model:
#         save_model_dir = os.path.split(opts.save_model_path)[0]
#         if not os.path.exists(save_model_dir):
#             os.makedirs(save_model_dir)

#     if opts.log_path:
#         log_dir = os.path.split(opts.log_path)[0]
#         if not os.path.exists(log_dir):
#             os.makedirs(log_dir)
#     if opts.tensorboard_log_dir:
#         if not os.path.exists(opts.tensorboard_log_dir):
#             os.makedirs(opts.tensorboard_log_dir)
#     return opts


# def get_inference_config():
#     parser = ArgumentParser(description='train')
#     add_config_opts(parser)
#     add_general_opts(parser)
#     add_inference_opts(parser)
#     add_model_opts(parser)
#     add_log_opts(parser, is_train=False)
#     add_reproducibility_opts(parser)
#     opts, unknown_opts = parser.parse_known_args()
#     if unknown_opts:
#         print("unknown_opts:", unknown_opts)

#     opts.device = torch.device(f'cuda:{opts.gpu_id}' if torch.cuda.is_available() else 'cpu')

#     # check
#     if opts.log_path:
#         log_dir = os.path.split(opts.log_path)[0]
#         if not os.path.exists(log_dir):
#             os.makedirs(log_dir)
#     return opts
