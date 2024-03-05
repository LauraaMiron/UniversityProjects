package com.example.myplantapp

import PlantsAdapter
import android.content.Intent
import android.os.Bundle
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.myplantapp.databinding.ActivityMainBinding


class MainActivity : AppCompatActivity() { // enables compatible features on older Android versions
    // allows easy access to views in the layout
    private lateinit var binding: ActivityMainBinding
    private lateinit var db: PlantDatabaseHelper
    private lateinit var plantsAdapter: PlantsAdapter

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // binds the activity with the corresponding XML file
        binding = ActivityMainBinding.inflate(layoutInflater) // ->converts XML into Views

        setContentView(binding.root)

        fun goToList(){
            val intent  = Intent(this, ListViewActivity::class.java)
            startActivity(intent);
        }


        val startButton = findViewById<Button>(R.id.startButton);
        startButton.setOnClickListener{
            goToList()
        }
    }

// called when the activity is brought to the foreground
//    override fun onResume() {
//        super.onResume()
//        plantsAdapter.refreshData(db.getAllPlants())
//    }
}