module.exports = {
  apps: [{
    name: "gettr-archiver",
    script: "./main.py"
    interpreter: "python3"
    env: {
      "GETTR_DATA_PATH": "~/gettr.db",
    }],
  autorestart: false,
}
