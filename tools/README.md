# Ryno-Tec Tools

Standalone command-line tools for Ryno-Tec Consulting business operations.

## Quote Generator

Generate professional, SA-compliant quotes for tender bids and client proposals.

**Works offline** — no Cloud subscription required. Uses the invoice-quote-generator module locally.

### Installation

```bash
cd /home/claude/ryno-tec-consulting
pip install -r modules/invoice-quote-generator/requirements.txt
```

### Usage

#### Interactive Mode (Recommended)

```bash
python tools/quote-generator.py --interactive
```

You'll be prompted for:
- Client name and email
- Tender reference (optional)
- Service line (platform, azure, or ai)
- Quote amount and quantity
- Due date
- Additional notes

#### Command-Line Mode

```bash
python tools/quote-generator.py \
  --client "Department of Finance" \
  --service platform \
  --amount 1500000 \
  --tender "RFQ-2026-001" \
  --email procurement@dept.gov.za \
  --output quotes/
```

#### Quick Examples

**Platform Engineering quote:**
```bash
python tools/quote-generator.py --interactive
# Enter: Client Name, Service: platform, Amount: 1500000
```

**Multiple quotes from tenders:**
```bash
# RFQ 1
python tools/quote-generator.py \
  --client "Enterprise A" \
  --service azure \
  --amount 400000 \
  --tender "RFQ-001-2026"

# RFQ 2
python tools/quote-generator.py \
  --client "Enterprise B" \
  --service ai \
  --amount 800000 \
  --tender "RFQ-002-2026"
```

### Options

```
--interactive, -i       Interactive mode (prompts for all details)
--client, -c            Client name
--email, -e             Client email (default: procurement@client.co.za)
--service, -s           Service: platform, azure, or ai
--amount, -a            Quote amount in ZAR
--quantity, -q          Quantity (default: 1)
--tender, -t            Tender reference number
--due-days, -d          Days until due date (default: 30)
--notes, -n             Additional notes
--output, -o            Output directory (default: quotes/)
```

### Services

- **platform** — Platform Engineering & DevOps (Infrastructure as Code, DevOps, Cloud-native)
- **azure** — Azure Modern Workplace Management (AVD, Entra ID, Intune, M365)
- **ai** — AI Infrastructure & MLOps (ML pipelines, model deployment, AI governance)

### Output

Quotes are saved as PDF files in the format:
```
Quote_<ClientName>_<TenderRef>_<Date>.pdf
```

Example:
```
Quote_DeptOfFinance_RFQ2026001_20261012.pdf
```

Each quote includes:
- Ryno-Tec company details and branding
- Client information and tender reference
- Service description and pricing
- VAT calculation (15%)
- B-BBEE level and compliance notation
- Professional indemnity insurance reference
- Payment terms and due date

### Workflow Integration

**With eTender Pro and Ryno-Tec Hub:**

1. **Discover** → Find tender in eTender Pro or Ryno-Tec Business Hub
2. **Generate** → Run quote-generator.py (interactive or CLI)
3. **Review** → Open the generated PDF locally
4. **Store** → Upload PDF to Ryno-Tec Hub's invoices collection
5. **Submit** → Attach quote to your tender bid on eTenders portal

### Offline Use

This tool works completely offline:
- ✓ No internet connection required after dependencies installed
- ✓ No Claude subscription needed
- ✓ No external services called
- ✓ Data stays on your computer
- ✓ Generates PDFs locally

### Troubleshooting

**Module not found error:**
```bash
# Ensure you're in the repo directory
cd /home/claude/ryno-tec-consulting

# Install dependencies
pip install reportlab jinja2 pydantic python-dateutil
```

**Permission denied:**
```bash
chmod +x tools/quote-generator.py
```

**Invalid service error:**
Use one of: `platform`, `azure`, `ai` (not the full service name)

### Roadmap

- [ ] Config file support (default company details, output paths)
- [ ] Batch generation from CSV (multiple quotes at once)
- [ ] Quote template customization
- [ ] Hub integration (save quotes directly to artifact database)
- [ ] Invoice generation from approved quotes
- [ ] Email delivery integration

---

**Author:** Kagiso Tshukudu  
**Version:** 1.0.0  
**Last Updated:** 2026-10-12
