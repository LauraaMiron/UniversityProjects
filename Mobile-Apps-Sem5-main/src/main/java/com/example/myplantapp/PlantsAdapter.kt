import android.content.Context
import android.content.Intent
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.TextView
import android.widget.Toast
import androidx.recyclerview.widget.RecyclerView
import com.example.myplantapp.Plant
import com.example.myplantapp.PlantDatabaseHelper
import com.example.myplantapp.UpdatePlantActivity
import com.example.myplantapp.R

class PlantsAdapter(private var plants: List<Plant>, context: Context) :
    RecyclerView.Adapter<PlantsAdapter.PlantViewHolder>() {

    private val db: PlantDatabaseHelper = PlantDatabaseHelper(context)

    class PlantViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val nameTextView: TextView = itemView.findViewById(R.id.nameTextView)
        val lastWateredTextView: TextView = itemView.findViewById(R.id.lastWateredTextView)
        val wateringIntervalTextView: TextView = itemView.findViewById(R.id.wateringIntervalTextView)
        var updateButton: ImageView = itemView.findViewById(R.id.updateButton)
        var deleteButton: ImageView = itemView.findViewById(R.id.deleteButton)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): PlantViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.plant_item, parent, false)
        return PlantViewHolder(view)
    }

    override fun getItemCount(): Int {
        return plants.size
    }

    override fun onBindViewHolder(holder: PlantViewHolder, position: Int) {
        val plant = plants[position]
        holder.nameTextView.text = plant.name
        holder.lastWateredTextView.text = plant.lastWatered.toString() // You may want to format this date
        holder.wateringIntervalTextView.text = plant.wateringInterval.toString()

        holder.updateButton.setOnClickListener {
            val intent = Intent(holder.itemView.context, UpdatePlantActivity::class.java).apply {
                putExtra("plant_id", plant.id)
            }
            holder.itemView.context.startActivity(intent)
        }

        holder.deleteButton.setOnClickListener {
            db.deletePlant(plant.id)
            refreshData(db.getAllPlants())
            Toast.makeText(holder.itemView.context, "Plant deleted", Toast.LENGTH_SHORT).show()
        }
    }

    fun refreshData(newPlants: List<Plant>) {
        plants = newPlants
        notifyDataSetChanged()
    }
}
