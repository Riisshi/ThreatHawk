from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime, UTC

Base = declarative_base()

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)

    timestamp = Column(DateTime)
	
    event_type = Column(String)
    source_ip = Column(String)
    raw_log = Column(String, unique=True)

class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)

    timestamp = Column(DateTime)

    alert_type = Column(String)

    severity = Column(String)

    source_ip = Column(String)

    description = Column(String)
