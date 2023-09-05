from autogameplayer.utils import set_random_seed
from autogameplayer.utils.configs.get_configs import get_start_config
from autogameplayer.game import window_info
# from autogameplayer.game.superworld.run import main as superworldrun
# from autogameplayer.game.tft.run import main as tftrun

def main():
    opt = get_start_config()
    # set_random_seed(opt.seed)

    start_str = " | ".join([f"{i}: {k}" for i, k in enumerate(window_info.keys())])
    game_num = input("We provide following games:\n"+start_str+"\nplease select game:")    

    try:
        key = list(window_info.keys())[int(game_num)]
        print("game num:", game_num)
        print("key:", key)
        print("value:", window_info[key])

        if key == "superworld":
            # superworldrun(**window_info[key])
            pass
        elif key == "tft":
            # tftrun(**window_info[key])
            pass
        else:
            raise NotImplementedError("")
    except:
        print(f"Wrong input {game_num}")



if __name__ == "__main__":
    main()
