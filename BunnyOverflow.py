from BunnyConfig import BunnyConfig
from BunnyMenu import BunnyMenu
from BunnyBanners import BunnyBanners
from BunnyPreReqs import BunnyPreReqs


if __name__ == '__main__':
    BunnyBanners.PrintMainBanner()

    BunnyPreReqs.CheckForPreReqs()

    config = BunnyConfig()
    config.LoadConfig(True)

    BunnyMenu.config = config

    BunnyMenu.GetUserSelection()
