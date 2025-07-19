from .logger import VenusConsole

vc = VenusConsole()

vc.info("Venus Console initialized successfully.")
vc.warn("OPENAI API key is not set. Some features may not work as expected.")
vc.kill("Module raised an exception. Please check the logs for details.")
