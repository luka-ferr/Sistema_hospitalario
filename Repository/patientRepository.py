"""Interfaz"""
from abc import ABC, abstractmethod


class PatientRepository(ABC):

    @abstractmethod
    def save(self, paciente):
        pass

    @abstractmethod
    def find_by_name(self, patient_id):
        pass

    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def update(self, paciente):
        pass

    @abstractmethod
    def delete(self, patient_id):
        pass