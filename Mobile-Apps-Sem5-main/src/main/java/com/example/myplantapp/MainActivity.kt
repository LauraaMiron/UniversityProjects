package com.example.myplantapp

import PlantsAdapter
import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.myplantapp.databinding.ActivityMainBinding


class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding
    private lateinit var db: PlantDatabaseHelper
    private lateinit var plantsAdapter: PlantsAdapter

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)

        setContentView(binding.root)

        db = PlantDatabaseHelper(this)
        plantsAdapter = PlantsAdapter(db.getAllPlants(), this)

        binding.plantsRecyclerView.layoutManager = LinearLayoutManager(this)
        binding.plantsRecyclerView.adapter = plantsAdapter

        binding.addButton.setOnClickListener {
            val intent = Intent(this, AddPlantActivity::class.java)
            startActivity(intent)
        }
    }

    override fun onResume() {
        super.onResume()
        plantsAdapter.refreshData(db.getAllPlants())
    }
}