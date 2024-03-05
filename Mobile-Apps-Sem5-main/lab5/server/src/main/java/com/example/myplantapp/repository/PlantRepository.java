package com.example.myplantapp.repository;

import com.example.myplantapp.model.Plant;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;


@Repository
public interface PlantRepository extends JpaRepository<Plant, Integer> {
}
