package com.example.myplantapp

import android.content.ContentValues
import android.content.Context
import android.database.sqlite.SQLiteDatabase
import android.database.sqlite.SQLiteOpenHelper
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Locale
import android.util.Log


class PlantDatabaseHelper(context: Context) : SQLiteOpenHelper(context, context.getDatabasePath(DATABASE_NAME).absolutePath, null, DATABASE_VERSION) {

    companion object {
        private const val DATABASE_NAME = "plantsapp.db"
        private const val DATABASE_VERSION = 1
        private const val TABLE_NAME = "allplants"
        private const val COLUMN_ID = "id"
        private const val COLUMN_NAME = "name"
        private const val COLUMN_LAST_WATERED = "last_watered"
        private const val COLUMN_WATERING_INTERVAL = "watering_interval"
    }

    override fun onCreate(db: SQLiteDatabase?) {
        val createTableQuery = "CREATE TABLE $TABLE_NAME ($COLUMN_ID INTEGER PRIMARY KEY, $COLUMN_NAME TEXT, $COLUMN_LAST_WATERED TEXT, $COLUMN_WATERING_INTERVAL INTEGER)"
        db?.execSQL(createTableQuery)
    }

    override fun onUpgrade(db: SQLiteDatabase?, oldVersion: Int, newVersion: Int) {
        val dropTableQuery = "DROP TABLE IF EXISTS $TABLE_NAME"
        db?.execSQL(dropTableQuery)
        onCreate(db)
    }

    fun insertPlant(plant: Plant) {
        val db = writableDatabase
        val values = ContentValues().apply {
            put(COLUMN_NAME, plant.name)
            put(COLUMN_LAST_WATERED, plant.lastWatered)
            put(COLUMN_WATERING_INTERVAL, plant.wateringInterval)
        }
        db.insert(TABLE_NAME, null, values)
        Log.d("PlantDatabaseHelper", "Inserted plant: ${plant.name}")
        db.close()
    }

    fun getAllPlants(): List<Plant> {
        val plantsList = mutableListOf<Plant>()
        val db = readableDatabase
        val query = "SELECT * FROM $TABLE_NAME"
        val cursor = db.rawQuery(query, null)

        while (cursor.moveToNext()) {
            val id = cursor.getInt(cursor.getColumnIndexOrThrow(COLUMN_ID))
            val name = cursor.getString(cursor.getColumnIndexOrThrow(COLUMN_NAME))
            val lastWatered = cursor.getString(cursor.getColumnIndexOrThrow(COLUMN_LAST_WATERED))
            val wateringInterval = cursor.getInt(cursor.getColumnIndexOrThrow(COLUMN_WATERING_INTERVAL))

            val plant = Plant(id, name, lastWatered, wateringInterval)
            plantsList.add(plant)
        }
        cursor.close()
        db.close()
        return plantsList
    }

    fun updatePlant(id: Int, plant: Plant) {
        val db = writableDatabase
        val values = ContentValues().apply {
            put(COLUMN_NAME, plant.name)
            put(COLUMN_LAST_WATERED, plant.lastWatered)
            put(COLUMN_WATERING_INTERVAL, plant.wateringInterval)
        }
        val whereClause = "$COLUMN_ID = ?"
        val whereArgs = arrayOf(id.toString())
        db.update(TABLE_NAME, values, whereClause, whereArgs)
        db.close()
    }

    fun getPlantById(plantId: Int): Plant {
        val db = readableDatabase
        val query = "SELECT * FROM $TABLE_NAME WHERE $COLUMN_ID = $plantId"

        val cursor = db.rawQuery(query, null)
        cursor.moveToFirst()

        val id = cursor.getInt(cursor.getColumnIndexOrThrow(COLUMN_ID))
        val name = cursor.getString(cursor.getColumnIndexOrThrow(COLUMN_NAME))
        val lastWatered = cursor.getString(cursor.getColumnIndexOrThrow(COLUMN_LAST_WATERED))
        val wateringInterval = cursor.getInt(cursor.getColumnIndexOrThrow(COLUMN_WATERING_INTERVAL))

        cursor.close()
        db.close()
        return Plant(id, name, lastWatered, wateringInterval)
    }

    fun deletePlant(plantId: Int) {
        val db = writableDatabase
        val whereClause = "$COLUMN_ID = ?"
        val whereArgs = arrayOf(plantId.toString())
        db.delete(TABLE_NAME, whereClause, whereArgs)
        db.close()
    }
}
