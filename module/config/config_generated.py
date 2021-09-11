import datetime

# This file was automatically generated by module/config/db.py.
# Don't modify it manually.


class GeneratedConfig:
    """
    Auto generated configuration
    """

    # Func `Alas`
    Scheduler_Enable = False
    Scheduler_NextRun = datetime.datetime(2020, 1, 1, 0, 0)
    Scheduler_Command = 'Alas'
    Scheduler_SuccessInterval = 0
    Scheduler_FailureInterval = 120
    Scheduler_ServerUpdate = '00:00'
    Emulator_Serial = '127.0.0.1:5555'
    Emulator_PackageName = 'com.bilibili.azurlane'
    Emulator_ScreenshotMethod = 'ADB'
    Emulator_ControlMethod = 'minitouch'
    Error_HandleError = True
    Error_SaveError = True
    Error_ScreenshotLength = 1
    DropRecord_SaveFolder = './screenshot'
    DropRecord_AzurStatsID = None
    DropRecord_SaveResearch = False
    DropRecord_UploadResearch = False
    DropRecord_SaveCommission = False
    DropRecord_UploadCommission = False
    DropRecord_SaveCombat = False

    # Func `Main`

    # Func `Commission`

    # Func `Research`
    ResearchInput_UseCube = False
    ResearchInput_UseCoin = True
    ResearchInput_UsePart = True
    ResearchOutput_PresetFilter = 'series_4'
    ResearchOutput_CustomFilter = '0.5 > reset > shortest'