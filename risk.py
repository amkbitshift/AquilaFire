def calculate_risk(temp, humidity, wind, smoke_conf):
    risk = (
        smoke_conf * 40 +
        (temp / 50) * 30 +
        (wind / 20) * 20 +
        ((100 - humidity) / 100) * 10
    )
    return min(int(risk), 100)
