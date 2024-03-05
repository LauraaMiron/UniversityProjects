package com.example.myplantapp

import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.example.myplantapp.databinding.ActivityUpdatePlantBinding

class UpdatePlantActivity : AppCompatActivity() {

    private lateinit var binding: ActivityUpdatePlantBinding
    private lateinit var db: PlantDatabaseHelper
    private var plantId: Int = -1

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        binding = ActivityUpdatePlantBinding.inflate(layoutInflater)
        setContentView(binding.root)

        db = PlantDatabaseHelper(this)

        plantId = intent.getIntExtra("plant_id", -1)
        if (plantId == -1) {
            finish()
            return
        }

        val plant = db.getPlantById(plantId)
        binding.updateNameEditText.setText(plant.name)
        binding.updateLastWateredEditText.setText(plant.lastWatered)
        binding.updateWateringIntervalEditText.setText(plant.wateringInterval.toString())

        binding.updateSaveButton.setOnClickListener {
            val newName = binding.updateNameEditText.text.toString()
            val newLastWatered = binding.updateLastWateredEditText.text.toString()
            val newWateringInterval = binding.updateWateringIntervalEditText.text.toString().toInt()

            val updatedPlant = Plant(plantId, newName, newLastWatered, newWateringInterval)
            db.updatePlant(plantId, updatedPlant)
            finish()
            Toast.makeText(this, "Changes Saved", Toast.LENGTH_SHORT).show()
        }
    }
}
