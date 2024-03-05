package com.example.myplantapp
import com.example.myplantapp.Plant
import retrofit2.Call
import retrofit2.Response
import retrofit2.http.*

interface PlantService {
    @GET("/plants/{id}")
    fun retrievePlant(@Path("id") id: Int) : Call<Plant>

    @GET("/plants")
    fun retrieveAllPlant() : Call<List<Plant>>

    @DELETE("/plants/{id}")
    fun deletePlant(@Path("id") id: Int) : Call<Plant>

    @POST("/plants")
    fun createPlant(@Body plant: Plant) : Call<Plant>

    @PUT("/plants/{id}")
    fun updatePlant(@Path("id") id: Int, @Body plant: Plant) : Call<Plant>
}