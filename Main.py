from UI.UserInterface import UserInterface
from HostingService import HostingService

hostingService = HostingService()
userInterface = UserInterface(hostingService)

userInterface.start()
