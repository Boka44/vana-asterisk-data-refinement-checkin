const mongoose = require('mongoose')

const checkInSchema = new mongoose.Schema({
  user_hash: { type: String, required: true },
  timestamp: { type: Date, default: Date.now },
  checkinId: { type: String, required: true, unique: true },
  mood: String,
  health_comment: String,
  doctor_visit: Boolean,
  health_profile_update: Boolean,
  anxiety_level: Number,
  anxiety_details: String,
  pain_level: Number,
  pain_details: String,
  fatigue_level: Number,
  fatigue_details: String
})

module.exports = mongoose.model('CheckIn', checkInSchema)

// https://blue-yummy-rooster-621.mypinata.cloud/ipfs/bafkreicxmtu2eyp3mkj2kd3lp3cnhyqmu6sinhb3vcwn73gcvygwsxz2da

/*
50
Checkin Refiner
https://blue-yummy-rooster-621.mypinata.cloud/ipfs/bafkreicxmtu2eyp3mkj2kd3lp3cnhyqmu6sinhb3vcwn73gcvygwsxz2da
https://github.com/Boka44/vana-asterisk-data-refinement-checkin/releases/download/v7/refiner-7.tar.gz
0x04fdb1b931c1c61849105a11f02a6c1519ad5e248d682ce2f65351453ff42523f10b98f1d9cd1fe3f47cfe4223c827a4401fd4dda7c23c3bec7dc59359af9974a1
*/