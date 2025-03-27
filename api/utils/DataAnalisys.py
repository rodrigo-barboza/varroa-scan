class DataAnalisys:
    @staticmethod
    def calculate_infestation(predicted_info, total_bees, analized_images_count):
        infected_bees = sum(info['varroa_detected_count'] for info in predicted_info)
        infestation_percentage = (infected_bees / total_bees) * 100

        return {
            "varroa_detected_count": infected_bees,
            "infestation_level": DataAnalisys.get_infestation_level(infestation_percentage),
            "infestation_percent": infestation_percentage,
            "analized_images": analized_images_count,
        }

    @staticmethod
    def get_infestation_level(infestation_percentage):
        if infestation_percentage < 10:
            return "baixa"
        elif infestation_percentage < 50:
            return "média"
        else:
            return "alta"

