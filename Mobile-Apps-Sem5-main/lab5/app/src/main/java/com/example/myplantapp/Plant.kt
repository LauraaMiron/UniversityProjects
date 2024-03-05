package com.example.myplantapp

import java.io.Serializable

data class Plant(val id: Int, val name: String, val lastWatered: String, val wateringInterval: Int) :
    Serializable