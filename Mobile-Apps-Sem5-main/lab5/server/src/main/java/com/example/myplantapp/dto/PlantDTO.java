package com.example.myplantapp.dto;


import lombok.*;

@Data
@NoArgsConstructor
@AllArgsConstructor
@ToString
@EqualsAndHashCode
public class PlantDTO {

    private Integer id;

    private String name;

    private String lastWatered;

    private String wateringInterval;
}
