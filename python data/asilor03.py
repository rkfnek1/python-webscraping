import airtest
from airtest.core.api import connect_device

dev1 = connect_device("Android://127.0.0.1:5037/serialno1")
dev2 = connect_device("Android://127.0.0.1:5037/serialno1")



# current_dev = device()