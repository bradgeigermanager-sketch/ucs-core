import importlib
import pkgutil
import inspect
from .base import BaseTransformer

def load_transformers():
    """
    Dynamically imports modules from the transformers directory
    and registers subclasses of BaseTransformer.
    """
    transformers = {}
    
    # Iterate through all modules in the current directory
    for loader, module_name, is_pkg in pkgutil.iter_modules(__path__):
        if module_name == "base": continue  # Skip the base class
        
        # Import the module
        module = importlib.import_module(f".{module_name}", package=__name__)
        
        # Find classes in the module that inherit from BaseTransformer
        for name, obj in inspect.getmembers(module, inspect.isclass):
            if issubclass(obj, BaseTransformer) and obj is not BaseTransformer:
                # Use the module name (e.g., 'lcc') as the key
                transformers[module_name.upper()] = obj()
                
    return transformers

# Registry populated automatically
REGISTRY = load_transformers()

