package com.example.myplantapp.controller;

import com.example.myplantapp.converter.PlantConverter;
import com.example.myplantapp.dto.PlantDTO;
import com.example.myplantapp.model.Plant;
import com.example.myplantapp.repository.PlantRepository;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;

import java.util.Optional;
import java.util.Set;

@RestController
public class PlantController {

    private PlantRepository plantRepository;

    private PlantConverter plantConverter;

    public PlantController(PlantRepository plantRepository, PlantConverter plantConverter){
        this.plantRepository = plantRepository;
        this.plantConverter = plantConverter;
    }

    @GetMapping("/plants")
    public Set<PlantDTO> retrieveAllStories(){
        System.out.println("GET ALL");
        return plantConverter.convertModelsToDtos(plantRepository.findAll());
    }

    @PostMapping("/plants")
    public Plant createPlant(@RequestBody Plant plant){
        System.out.println("POST");

        return plantRepository.save(plant);
    }

    @DeleteMapping("/plants/{id}")
    public Plant deletePlant(@PathVariable int id) {
        System.out.println("DELETE");
        Optional<Plant> plantOptional = plantRepository.findById(id);

        if(plantOptional.isEmpty()){
            return null;
        }

        plantRepository.deleteById(id);
        return plantOptional.get();
    }

    @GetMapping("/")
    public ResponseEntity<String> getRoot() {
        return ResponseEntity.ok("Hello, this is the root endpoint!");
    }


    @PutMapping("/plants/{id}")
    public Plant updatePlant(@PathVariable int id, @RequestBody Plant plant){
        System.out.println("PUT");
        Optional<Plant> plantOptional = plantRepository.findById(id);

        if(plantOptional.isEmpty()){
            return null;
        }

        plant.setId(id);
        return plantRepository.save(plant);
    }

}
