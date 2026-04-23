def classify_risk(data):
    score = (
        data.temperatura * 1.2 +
        (100 - data.humedad) * 1.0 +
        data.viento * 1.5 +
        (1 - data.ndvi) * 100
    )

    if score < 80:
        return "BAJO"
    elif score < 150:
        return "MEDIO"
    elif score < 220:
        return "ALTO"
    else:
        return "CRITICO"
