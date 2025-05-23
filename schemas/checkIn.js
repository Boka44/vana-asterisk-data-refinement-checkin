const mongoose = require('mongoose')

const checkInSchema = new mongoose.Schema({
  user_hash: { type: String, required: true },
  timestamp: { type: Date, default: Date.now },
  mood: String,
  health_comment: String,
  doctor_visit: Boolean,
  health_profile_update: Boolean,
  anxiety_level: String,
  anxiety_details: String,
  pain_level: Number,
  pain_details: String,
  fatigue_level: Number,
  fatigue_details: String
})

module.exports = mongoose.model('CheckIn', checkInSchema)

// https://blue-yummy-rooster-621.mypinata.cloud/ipfs/bafkreihrxjyot24fw6qnvi4twmcqyocg3ipeimt54gdd7aqrm5c4tacjoq