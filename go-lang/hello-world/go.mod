module hello

go 1.15

replace custom-math => ../custom-math

require (
	custom-math v0.0.0-00010101000000-000000000000
	golang.org/x/text v0.3.3 // indirect
	rsc.io/quote v1.5.2
)
