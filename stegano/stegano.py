from stegano import lsb

secret = lsb.hide("cat.jpg", "universitan pelita bangsa")

secret.save("sat-sec.png")

print(lsb.reveal("cat-sec.png"))