package com.example.myplantapp.model;


import lombok.*;

import javax.persistence.*;

@Entity
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
@Table(name = "allplants")
public class Plant {

    @Id
    private Integer id;

    @Column(name = "name")
    private String name;

    @Column(name = "lastWatered")
    private String lastWatered;

    @Column(name = "wateringInterval")
    private String wateringInterval;
}
