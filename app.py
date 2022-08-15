{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "aa41483f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import datetime as dt\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import sqlalchemy\n",
    "from sqlalchemy.ext.automap import automap_base\n",
    "from sqlalchemy.orm import Session\n",
    "from sqlalchemy import create_engine, func\n",
    "from flask import Flask, jsonify"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "83ad2797",
   "metadata": {},
   "outputs": [],
   "source": [
    "engine = create_engine(\"sqlite:///hawaii.sqlite\")\n",
    "Base = automap_base()\n",
    "Base.prepare(engine, reflect=True)\n",
    "Measurement = Base.classes.measurement\n",
    "Station = Base.classes.station\n",
    "session = Session(engine)\n",
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "46cb90ba",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (2734072857.py, line 13)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"/var/folders/ft/_td1458s54jg5065d4j5315w0000gn/T/ipykernel_43736/2734072857.py\"\u001b[0;36m, line \u001b[0;32m13\u001b[0m\n\u001b[0;31m    flask run\u001b[0m\n\u001b[0m            ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "@app.route(\"/\")\n",
    "\n",
    "def welcome():\n",
    "    return(\n",
    "    '''\n",
    "    Welcome to the Climate Analysis API!\n",
    "    Available Routes:\n",
    "    /api/v1.0/precipitation\n",
    "    /api/v1.0/stations\n",
    "    /api/v1.0/tobs\n",
    "    /api/v1.0/temp/start/end\n",
    "    ''')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "e3e5f207",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/api/v1.0/precipitation\")\n",
    "\n",
    "def precipitation():\n",
    "   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)\n",
    "   precipitation = session.query(Measurement.date, Measurement.prcp).\\\n",
    "   filter(Measurement.date >= prev_year).all()\n",
    "   precip = {date: prcp for date, prcp in precipitation}\n",
    "   return jsonify(precip)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "2cb176c1",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/api/v1.0/stations\")\n",
    "def stations():\n",
    "    results = session.query(Station.station).all()\n",
    "    stations = list(np.ravel(results))\n",
    "    return jsonify(stations=stations)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "35fff099",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "PythonData",
   "language": "python",
   "name": "pythondata"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
