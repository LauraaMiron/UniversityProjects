package com.example.myplantapp

import PlantsAdapter
import android.app.Activity
import android.app.AlertDialog
import android.content.Intent
import android.database.sqlite.SQLiteDatabase
import android.net.ConnectivityManager
import android.net.Network
import android.net.NetworkCapabilities
import android.os.Bundle
import android.util.Log
import android.view.Window
import android.widget.Toast
import androidx.activity.result.contract.ActivityResultContracts
import androidx.appcompat.app.AppCompatActivity
import androidx.core.content.ContextCompat
import androidx.lifecycle.lifecycleScope
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.myplantapp.databinding.ActivityStartBinding
import kotlinx.coroutines.launch
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response



class ListViewActivity : AppCompatActivity() {

    private lateinit var dbHelper: PlantDatabaseHelper
    private lateinit var database: SQLiteDatabase
    private lateinit var plantsAdapter: PlantsAdapter
    private lateinit var binding: ActivityStartBinding
    private var context = this

    private fun isNetworkConnected(): Boolean {
        val connectivityManager = getSystemService(CONNECTIVITY_SERVICE) as ConnectivityManager
        val activeNetwork = connectivityManager.activeNetwork
        val networkCapabilities = connectivityManager.getNetworkCapabilities(activeNetwork)
        return networkCapabilities != null &&
                networkCapabilities.hasCapability(NetworkCapabilities.NET_CAPABILITY_INTERNET)
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityStartBinding.inflate(layoutInflater)
        setContentView(binding.root)

        supportActionBar?.hide()
        val window: Window = this@ListViewActivity.window
        window.statusBarColor = ContextCompat.getColor(this@ListViewActivity, R.color.black)

        dbHelper = PlantDatabaseHelper(this)
        database = dbHelper.writableDatabase

        plantsAdapter = PlantsAdapter(dbHelper.getAllPlants(), this)
        binding.plantsRecyclerView.layoutManager = LinearLayoutManager(context)
        binding.plantsRecyclerView.adapter = plantsAdapter

        if (!isNetworkConnected()) {
            showDialog()
        }

        val connectivityManager = getSystemService(CONNECTIVITY_SERVICE) as ConnectivityManager
        connectivityManager.registerDefaultNetworkCallback(object :
            ConnectivityManager.NetworkCallback() {
            override fun onAvailable(network: Network) {
                lifecycleScope.launch {
                    // Retrieve all plants from the server
                    PlantAPI.retrofitService.retrieveAllPlant()
                        .enqueue(object : Callback<List<Plant>?> {
                            override fun onResponse(
                                call: Call<List<Plant>?>,
                                response: Response<List<Plant>?>
                            ) {

                                val plantsServer = response.body()!!
                                Log.d("Plants server", plantsServer.toString())
                                val plantsDatabase = dbHelper.getAllPlants();

                                for (p1: Plant in plantsDatabase) {
                                    var exists = false
                                    for (p2: Plant in plantsServer) {
                                        if (p1.id.equals(p2.id)) {
                                            exists = true
                                        }
                                    }

                                    if (!exists) {
                                        PlantAPI.retrofitService.createPlant(p1)
                                            .enqueue(object : Callback<Plant?> {
                                                override fun onResponse(
                                                    call: Call<Plant?>,
                                                    response: Response<Plant?>
                                                ) {
                                                    Log.d(
                                                        "Added item from local db",
                                                        "Success: " + p1
                                                    )
                                                }

                                                override fun onFailure(
                                                    call: Call<Plant?>,
                                                    t: Throwable
                                                ) {
                                                    Toast.makeText(
                                                        context,
                                                        "Failed to add item from local db!",
                                                        Toast.LENGTH_SHORT
                                                    ).show()
                                                    Log.d(
                                                        "Added item from local db",
                                                        "Failed: " + t.message
                                                    )
                                                }
                                            })
                                    }

                                }


                                for (p2: Plant in plantsServer) {
                                    var exists = false
                                    for (p1: Plant in plantsDatabase) {
                                        if (p1.id.equals(p2.id)) {
                                            exists = true
                                        }
                                    }

                                    if (!exists) {
                                        PlantAPI.retrofitService.deletePlant(p2.id)
                                            .enqueue(object : Callback<Plant?> {
                                                override fun onResponse(
                                                    call: Call<Plant?>,
                                                    response: Response<Plant?>
                                                ) {

//                                                plants.remove(p2)
                                                    Log.d(
                                                        "Deleted item from server",
                                                        "Success!"
                                                    )
                                                }

                                                override fun onFailure(
                                                    call: Call<Plant?>,
                                                    t: Throwable
                                                ) {
                                                    Toast.makeText(
                                                        context,
                                                        "Failed to remove item from server!",
                                                        Toast.LENGTH_SHORT
                                                    ).show()
                                                    Log.d(
                                                        "Deleted item from server",
                                                        "Failed! " + t.message
                                                    )
                                                }
                                            })
                                    }
                                }


                                for (p1: Plant in plantsDatabase) {
                                    var different = false
                                    for (p2: Plant in plantsServer) {
                                        if (p1.id.equals(p2.id) && ((!p1.name.equals(p2.name) || !p1.lastWatered.equals(p2.lastWatered)
                                                    || !p1.wateringInterval.equals(p2.wateringInterval)))
                                        ) {
                                            different = true
                                            Log.d(
                                                "Updated item from the server",
                                                "Success: " + p2
                                            )
                                        }
                                    }

                                    if (different) {
                                        PlantAPI.retrofitService.updatePlant(p1.id, p1)
                                            .enqueue(object : Callback<Plant?> {
                                                override fun onResponse(
                                                    call: Call<Plant?>,
                                                    response: Response<Plant?>
                                                ) {
                                                    Log.d(
                                                        "Updated item from the server",
                                                        "Success: " + p1
                                                    )
                                                }

                                                override fun onFailure(
                                                    call: Call<Plant?>,
                                                    t: Throwable
                                                ) {
                                                    Toast.makeText(
                                                        context,
                                                        "Failed to update item from server!",
                                                        Toast.LENGTH_SHORT
                                                    ).show()
                                                    Log.d(
                                                        "Updated item from the server",
                                                        "Failed: " + t.message
                                                    )
                                                }
                                            })
                                    }

                                }
                            }

                            override fun onFailure(call: Call<List<Plant>?>, t: Throwable) {
                                lifecycleScope.launch {
                                    Toast.makeText(
                                        context,
                                        "Failed to check differences between local db and server!",
                                        Toast.LENGTH_SHORT
                                    ).show()
                                    Log.d(
                                        "Check for differences between local db and server",
                                        "Failed: " + t.message
                                    )
                                }
                            }

                        })
                }
            }
        }
        )

        var resultLauncher = registerForActivityResult(ActivityResultContracts.StartActivityForResult()) { result ->
            if (result.resultCode == Activity.RESULT_OK) {
                // There are no request codes
                val data: Intent? = result.data
            }
        }

        binding.addButton.setOnClickListener {
            val intent = Intent(applicationContext, AddPlantActivity::class.java)
            resultLauncher.launch(intent)
        }
    }

    private fun showDialog() {
        AlertDialog.Builder(this).setTitle("No Internet Connection")
            .setMessage("Fallback on local DB")
            .setPositiveButton(android.R.string.ok) { _, _ -> }
            .setIcon(android.R.drawable.ic_dialog_alert).show()
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)

        if (resultCode == Activity.RESULT_OK) {
            when (requestCode) {
                3 -> {
                    if (data != null) {
                        val plant = data.getSerializableExtra<Plant>("plant", Plant::class.java)
                        if (plant != null) {
                            addPlant(plant)
                            Toast.makeText(this, "Added!", Toast.LENGTH_SHORT).show()
                        }
                    }
                }
                5 -> {
                    if (data != null) {
                        val plant = data.getSerializableExtra<Plant>("plant", Plant::class.java)
                        if (plant != null) {
                            val id = data.getIntExtra("id", -1)
                            updatePlant(id, plant)
                            Toast.makeText(this, "Updated!", Toast.LENGTH_SHORT).show()
                        }
                    }
                }
            }
        }
    }

    fun deletePlant(id: Int) {
        if (isNetworkConnected()) {
            lifecycleScope.launch {
                PlantAPI.retrofitService.deletePlant(id).enqueue(object : Callback<Plant?> {
                    override fun onResponse(call: Call<Plant?>, response: Response<Plant?>) {
                        dbHelper.deletePlant(id)
                        binding.plantsRecyclerView.adapter?.notifyDataSetChanged()
                        Log.d("Delete plant action - server", "Success: " + response.body())
                    }

                    override fun onFailure(call: Call<Plant?>, t: Throwable) {
                        Toast.makeText(
                            context,
                            "Failed to delete plant" + t.message,
                            Toast.LENGTH_SHORT
                        ).show()
                        Log.d("Delete plant action - server", "Failed: " + t.message)
                    }
                })
            }

        } else {
            showDialog()
            dbHelper.deletePlant(id)
            Log.d("Delete plant action - local database", "Success!")
        }
        binding.plantsRecyclerView.adapter?.notifyDataSetChanged()

    }

    fun updatePlant(id: Int, plant: Plant) {
        if (isNetworkConnected()) {
            lifecycleScope.launch {
                PlantAPI.retrofitService.updatePlant(id, plant).enqueue(object : Callback<Plant?> {
                    override fun onResponse(call: Call<Plant?>, response: Response<Plant?>) {
                        dbHelper.updatePlant(id, plant)
                        binding.plantsRecyclerView.adapter?.notifyDataSetChanged()
                        Log.d("Update plant action - server", "Success: " + response.body())
                    }

                    override fun onFailure(call: Call<Plant?>, t: Throwable) {
                        Toast.makeText(
                            context,
                            "Failed to update plant!" + t.message,
                            Toast.LENGTH_SHORT
                        ).show()
                        Log.d("Update plant action - server", "Failed: " + t.message)
                    }
                })
            }
        } else {
            showDialog()
            dbHelper.updatePlant(id, plant)
            binding.plantsRecyclerView.adapter?.notifyDataSetChanged()
            Log.d("Update plant action - local database", "Success!")
        }
    }

    fun addPlant(plant: Plant) {
        if (isNetworkConnected()) {
            lifecycleScope.launch {
                PlantAPI.retrofitService.createPlant(plant).enqueue(object : Callback<Plant?> {
                    override fun onResponse(call: Call<Plant?>, response: Response<Plant?>) {
                        binding.plantsRecyclerView.adapter?.notifyDataSetChanged()
                        Log.d("Add plant action - server", "Success: " + response.body().toString())
                    }

                    override fun onFailure(call: Call<Plant?>, t: Throwable) {
                        Toast.makeText(
                            context,
                            "Failed to add plant!" + t.message,
                            Toast.LENGTH_SHORT
                        ).show()
                        Log.d("Add plant action - server", "Failed: " + t.message)
                    }
                })
            }
        } else {
            showDialog()
            binding.plantsRecyclerView.adapter?.notifyDataSetChanged()
            Log.d("Add plant action - local database", "Success!")
        }
    }
    override fun onResume() {
        super.onResume()
        plantsAdapter.refreshData(dbHelper.getAllPlants())
    }


}