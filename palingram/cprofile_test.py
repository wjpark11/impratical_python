"""module for profiling find_palingram function"""
import cProfile
from palingram import find_palingrams
from palingram_optimized import find_palingrams_optimized

cProfile.run('find_palingrams_optimized()')
