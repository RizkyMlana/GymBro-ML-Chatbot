def get_bmi_recommendation(bmi):
    if bmi < 18.5:
        return "Kamu underweight. Disarankan menambah berat badan dengan asupan kalori yang cukup dan olahraga rutin."
    elif 18.5 <= bmi < 24.9:
        return "Berat badan kamu ideal. Pertahankan pola hidup sehat!"
    elif 25 <= bmi < 29.9:
        return "Kamu overweight. Disarankan mengatur pola makan dan menambah aktivitas fisik."
    else:
        return "Kamu mengalami obesitas. Sebaiknya konsultasikan ke dokter untuk program penurunan berat badan."
