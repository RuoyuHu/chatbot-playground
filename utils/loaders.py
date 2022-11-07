import torch
from transformers import AutoTokenizer, TextGenerationPipeline


device = 'cuda' if torch.cuda.is_available() else 'cpu'
device_id = 0 if device == 'cuda' else -1

def load_opt_for_generation(**kwargs):
    """
    Custom load function for OPT models
    """
    from transformers import OPTForCausalLM
    model_type = kwargs['model_type']
    model = OPTForCausalLM.from_pretrained(model_type).to(device)
    tokenizer = AutoTokenizer.from_pretrained(model_type)
    pipeline = TextGenerationPipeline(model=model, tokenizer=tokenizer, device=device_id)

    return model, tokenizer, pipeline

# Model type to load function mapping
model_type_to_func = {
    "opt-2.7b": load_opt_for_generation,
    "opt-350m": load_opt_for_generation,
}


def load_model_for_generation(**kwargs):
    """
    Load model function endpoint, should be only part of this module exposed to
    external modules
    """
    return model_type_to_func[kwargs['model_type']](**kwargs)
