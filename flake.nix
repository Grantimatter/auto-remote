{
  description = "A devShell example";

  inputs = {
    nixpkgs.url      = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url  = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        overlays = [ ];
        pkgs = import nixpkgs {
          inherit system overlays;
        };
        buildInputs = with pkgs; [
           python312Packages.python-lsp-server
        ];
      in
      {
        devShells.default = with pkgs; mkShell {
          buildInputs = [
            python312Packages.python-lsp-server
          ] ++ buildInputs;

          shellHook = ''
            alias ls=eza
            alias find=fd
          '';
        };
      }
    );
}
