from datetime import datetime
now = datetime.now().minute
i = now //5
d = now - (i * 5)
c = "зелёный" if d <3 else "красный"
print(c)