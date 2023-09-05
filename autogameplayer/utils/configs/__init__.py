#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   opts.py
@Time    :   2022/05/20 21:11:54
@Author  :   Mei Yu 
@Version :   1.0
@Desc    :   None
'''

from secrets import choice


def add_config_opts(parser):
    group = parser.add_argument_group('Configuration')
    group.add('-config', '--config', required=False,
              is_config_file_arg=True,
              help='the yaml config file path')


def add_general_opts(parser):
    group = parser.add_argument_group('General')
    group.add_argument('-dataset', '--dataset', default='uspto50k',
                        choices=['uspto50k', 'usptofull', 'mit', 'pistachio', 'customize'],
                        help='dataset name')


# def add_ai_general_opts(parser):
#     group = parser.add_argument_group('AIGeneral')
#     group.add_argument('-dataset', '--dataset', default='uspto50k',
#                         choices=['uspto50k', 'usptofull', 'mit', 'pistachio', 'customize'],
#                         help='dataset name')

#     group.add_argument('-gpu_id', '--gpu_id', type=int, default=0, 
#                         help='GPU device id')

#     # exp data config
#     group.add_argument('-rxn_type', '--rxn_type', action="store_true",
#                         help='has rxn type or not')
    
#     group.add_argument('-n_jobs', '--n_jobs', type=int, default=1, 
#                         help='number of workers')

#     group.add_argument('-train', '--train', action="store_true",
#                         help='train')
                        
#     # checkpoint
#     group.add_argument('-load_from_ckpt', '--load_from_ckpt', type=str,
#                         help='ckpt path')


# def add_dataset_preprocess_opts(parser):
#     group = parser.add_argument_group('Dataset Preprocess')
#     group.add_argument('-paths', '--paths', type=str, nargs="+",
#                         help='dataset path list')


# def add_train_opts(parser):
#     group = parser.add_argument_group('Train')
#     group.add_argument('-epochs', '--epochs', type=int, default=10, 
#                         help='epochs')
#     group.add_argument('-batch_size', '--batch_size', type=int, 
#                         default=128, help='batch_size')
#     group.add_argument('-valid_batch_size', '--valid_batch_size', 
#                         type=int, default=128, help='valid_batch_size')
#     group.add_argument('-valid_every_epochs', '--valid_every_epochs', 
#                         type=int, default=2, help='valid every . epochs')
#     group.add_argument('-expect_loss', '--expect_loss', 
#                         type=float, default=0.05, help='expect_loss')
#     group.add_argument('-expect_acc', '--expect_acc', 
#                         type=float, default=0.65, help='expect_acc')
#     group.add_argument('-report_acc', '--report_acc', action="store_true",
#                         help='report_acc')
#     group.add_argument('-save_model_path', '--save_model_path', type=str,
#                         default="", help='save_model_path')
                    

# def add_inference_opts(parser):
#     group = parser.add_argument_group('Inference')
#     group.add_argument('-models', '--models', nargs='+', type=str, 
#                         default=[], required=False,
#                         help="Path to model .pt file(s). ")
#     group.add_argument('-batch_size', '--batch_size', type=int, 
#                         default=128, help='batch_size')

# def add_model_opts(parser):
#     group = parser.add_argument_group('Model')
#     group.add_argument('-num_layers', '--num_layers', 
#                         type=int, default=3, help='num gnn layers')
#     group.add_argument('-residual', '--residual', action="store_true",
#                         help='residual')
    
#     # activation
#     group.add_argument('-activation', '--activation', default='relu',
#                     choices=['elu', 'relu', 'tanh'],
#                     help='activation function name')

#     # optimizer
#     group.add_argument('-learning_rate', '--learning_rate', 
#                         type=float, default=5e-4, help='learning_rate')
#     group.add_argument('-scheduler_step_size', '--scheduler_step_size', 
#                         type=int, default=20, help='scheduler_step_size')
#     group.add_argument('-scheduler_gamma', '--scheduler_gamma', 
#                         type=float, default=0.2, help='scheduler_gamma')


def add_reproducibility_opts(parser):
    group = parser.add_argument_group('Reproducibility')
    group.add_argument('-seed', '--seed', type=int, default=97,
                        help="Set random seed used for reproducibility")


# def add_log_opts(parser, is_train=True):
#     group = parser.add_argument_group('Log')
#     group.add_argument('-log_path', '--log_path', type=str,
#                         help="log file path")

#     # TODO:设计使得一些超参数可以分开
#     # if is_train:
#     group.add_argument('-report_every', '--report_every', type=int, default=50,
#                     help="print stats at this interval.")
#     group.add_argument('-tensorboard', '--tensorboard', action="store_true",
#                     help="use tensorboard to show .")
#     group.add_argument('-tensorboard_log_dir', '--tensorboard_log_dir', 
#                     type=str, help="log directory for Tensorboard. ")
#     # else:
#     #     # Options only during inference
#     #     pass


if __name__ == '__main__':
    from configargparse import ArgumentParser
    parser = ArgumentParser(description='test')
    add_config_opts(parser)
    add_general_opts(parser)
    # add_train_opts(parser)
    # add_model_opts(parser)
    # add_log_opts(parser, is_train=True)
    # add_reproducibility_opts(parser)
    opts, unknown_opts = parser.parse_known_args()
    print(opts)
    print(unknown_opts)
