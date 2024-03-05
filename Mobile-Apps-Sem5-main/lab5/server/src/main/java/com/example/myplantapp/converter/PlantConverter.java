package com.example.myplantapp.converter;

import com.example.myplantapp.dto.PlantDTO;
import com.example.myplantapp.model.Plant;
import org.springframework.stereotype.Component;

import java.util.Collection;
import java.util.Set;
import java.util.stream.Collectors;

@Component
public class PlantConverter implements Converter<Plant, PlantDTO>{

    public Set<Integer> convertModelsToIDs(Set<Plant> models) {
        return models.stream()
                .map(model -> model.getId())
                .collect(Collectors.toSet());
    }

    public Set<Integer> convertDTOsToIDs(Set<PlantDTO> dtos) {
        return dtos.stream()
                .map(dto -> dto.getId())
                .collect(Collectors.toSet());
    }

    public Set<PlantDTO> convertModelsToDtos(Collection<Plant> models) {
        return models.stream()
                .map(model -> convertModelToDto(model))
                .collect(Collectors.toSet());
    }

    public Set<Plant> convertDtosToModels(Collection<PlantDTO> dtos) {
        return dtos.stream()
                .map(this::convertDtoToModel)
                .collect(Collectors.toSet());
    }

    @Override
    public Plant convertDtoToModel(PlantDTO plantDTO) {
        Plant plant = new Plant(plantDTO.getId(), plantDTO.getName(), plantDTO.getLastWatered(), plantDTO.getWateringInterval());
//        story.setId(storyDTO.getId());
//        story.setTitle(storyDTO.getTitle());
//        story.setDate(storyDTO.getDate());
//        story.setEmotion(storyDTO.getEmotion());
//        story.setMotivationalMessage(storyDTO.getMotivationalMessage());
//        story.setText(storyDTO.getText());

        return plant;
    }

    @Override
    public PlantDTO convertModelToDto(Plant plant) {
        PlantDTO dto = new PlantDTO(plant.getId(), plant.getName(), plant.getLastWatered(), plant.getWateringInterval());

        return dto;
    }
}
