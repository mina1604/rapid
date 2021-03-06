#ifndef __TheoryAxioms__
#define __TheoryAxioms__

#include <memory>
#include <vector>

#include "Formula.hpp"
#include "Sort.hpp"
#include "Term.hpp"
#include "Expression.hpp"
#include "Variable.hpp"
#include "Program.hpp"
#include "Problem.hpp"

namespace analysis {

    class TheoryAxioms
    {
    public:
        TheoryAxioms() {}

         std::vector<std::shared_ptr<const logic::Axiom>> generate();

    private:
        void addZeroSmallestElementAxiom(std::vector<std::shared_ptr<const logic::Axiom>>& axioms);
        void addDefineSubEqAxiom(std::vector<std::shared_ptr<const logic::Axiom>>& axioms);
        void addMonotonicityAxiom(std::vector<std::shared_ptr<const logic::Axiom>>& axioms);
        void addTransitivityAxioms(std::vector<std::shared_ptr<const logic::Axiom>>& axioms);
        void addTotalityAxiom(std::vector<std::shared_ptr<const logic::Axiom>>& axioms);
        void addDisjointnessAxioms(std::vector<std::shared_ptr<const logic::Axiom>>& axioms);
    };
}
#endif
