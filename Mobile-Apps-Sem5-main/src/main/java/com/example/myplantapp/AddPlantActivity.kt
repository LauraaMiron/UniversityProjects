package com.example.myplantapp

import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.example.myplantapp.databinding.ActivityAddPlantBinding
import java.util.Date

class AddPlantActivity : AppCompatActivity() {

    private lateinit var binding: ActivityAddPlantBinding
    private lateinit var db: PlantDatabaseHelper

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityAddPlantBinding.inflate(layoutInflater)

        setContentView(binding.root)

        db = PlantDatabaseHelper(this)

        binding.saveButton.setOnClickListener {
            val name = binding.nameEditText.text.toString()
            val lastWatered = binding.lastWateredEditText.text.toString()
            val wateringInterval = binding.wateringIntervalEditText.text.toString().toIntOrNull() ?: 0

            val plant = Plant(0, name, lastWatered, wateringInterval)
            db.insertPlant(plant)

            finish()
            Toast.makeText(this, "Plant Saved", Toast.LENGTH_SHORT).show()
        }
    }
}